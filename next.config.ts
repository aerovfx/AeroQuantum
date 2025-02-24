/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  experimental: {
    appDir: true, // Nếu đang dùng Next.js 14+, kiểm tra lại flag này
  },
};

module.exports = nextConfig;