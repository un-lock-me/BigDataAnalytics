// This file configures the development web server
// which supports hot reloading and synchronized testing.

// Require Browsersync along with webpack and middleware for it
import browserSync from 'browser-sync';
import webpack from 'webpack';
import webpackDevMiddleware from 'webpack-dev-middleware';
import webpackHotMiddleware from 'webpack-hot-middleware';
import webpackConfigBuilder from './webpack.config';

const webpackConfig = webpackConfigBuilder;
const bundler = webpack(webpackConfig);

// Run Browsersync and use middleware for Hot Module Replacement
browserSync({
  port: (process.env.PORT || 3000),
  ui: {
    port: 3001
  },
  server: {
    baseDir: ''
    // middleware: [
    //   webpackDevMiddleware(bundler, {
    //     publicPath: webpackConfig.output.publicPath,
    //     stats: { colors: true },
    //     noInfo: true
    //     // for other settings see
    //     // http://webpack.github.io/docs/webpack-dev-middleware.html
    //   }),

      // webpackHotMiddleware(bundler)
    // ]
  },

  files: [
    '*.html'
  ]
});
