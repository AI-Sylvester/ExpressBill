import React, { useEffect } from 'react';
import { Capacitor } from '@capacitor/core';
import { BarcodeScanner } from '@capacitor-mlkit/barcode-scanning';
import { Html5QrcodeScanner } from 'html5-qrcode';
import { CameraAlt } from '@mui/icons-material'; // MUI camera icon
const Scanner = ({ onScan }) => {
  const isNative = Capacitor.isNativePlatform();

  const handleNativeScan = async () => {
    try {
      const result = await BarcodeScanner.scan();
      const code = result?.barcodes?.[0]?.rawValue;
      if (code) {
        onScan(code);
      } else {
        alert('No barcode found');
      }
    } catch (error) {
      console.error('Native scan failed:', error);
      alert('Failed to scan barcode');
    }
  };

  useEffect(() => {
    let scanner;

    if (!isNative) {
      scanner = new Html5QrcodeScanner(
        'html5qr-reader',
        { fps: 10, qrbox: 250 },
        false
      );

      scanner.render(
        (decodedText) => {
          onScan(decodedText);
        },
        (error) => {
          console.warn('QR scan error:', error);
        }
      );
    }

    return () => {
      if (scanner) {
        scanner.clear().catch((err) => console.error('Failed to clear scanner', err));
      }
    };
  }, [isNative, onScan]);

  return isNative ? (
   <div style={{ textAlign: 'center', marginTop: 20 }}>
      <button
        onClick={handleNativeScan}
        style={{
          width: 60,
          height: 60,
          backgroundColor: '#fa2056ff',
          color: '#fff',
          border: 'none',
          borderRadius: 8, // Square with slightly rounded corners
          cursor: 'pointer',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <CameraAlt style={{ fontSize: 28 }} />
      </button>
    </div>

  ) : (
    <div id="html5qr-reader" style={{ width: '100%' }} />
  );
};

export default Scanner;
