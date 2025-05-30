// vite.config.js
// This file is used to configure Vite for the Test Case Generator UI project.
// It sets up plugins, resolves aliases, and configures the development server proxy.
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
      '@services': path.resolve(__dirname, './src/services'),
      '@hooks': path.resolve(__dirname, './src/hooks'),
      '@utils': path.resolve(__dirname, './src/utils'),
    },
  },
  server: {
    proxy: {
    '/api': {
      target: 'http://api-layer-service:80',
      changeOrigin: true,
      rewrite: path => path.replace(/^\/api/, '/api'),
    },
  },
}
})