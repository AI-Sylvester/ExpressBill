import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.posapp.app',
  appName: 'Pos',
  webDir: 'build',
   server: {
    cleartext: true
  }
};

export default config;
