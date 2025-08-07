import { Html5Qrcode } from 'html5-qrcode';
import React, { useEffect } from 'react';

const QrScanner = ({ onScan }) => {
  useEffect(() => {
    const scanner = new Html5Qrcode("reader");

    // Define back camera constraints
    const config = {
      fps: 10,
      qrbox: 250,
      experimentalFeatures: {
        useBarCodeDetectorIfSupported: true,
      },
      videoConstraints: {
        facingMode: { exact: "environment" } // forces back camera
      }
    };

    scanner
      .start(
        { facingMode: { exact: "environment" } }, // try to use back camera
        config,
        (result) => {
          const code = typeof result === 'string' ? result : result?.text;
          if (code) onScan(code);
          scanner.stop().then(() => scanner.clear());
        },
        (error) => {
          // scanning errors like misreads
          console.warn("QR scan error", error);
        }
      )
      .catch((err) => {
        // init/start errors like camera permission or unavailability
        console.error("Failed to start scanner:", err);
      });

    return () => {
      scanner.stop().then(() => scanner.clear()).catch(() => {});
    };
  }, [onScan]);

  return <div id="reader" style={{ width: "100%" }} />;
};

export default QrScanner;
