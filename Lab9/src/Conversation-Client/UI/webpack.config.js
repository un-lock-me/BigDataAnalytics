var path = require('path');
var webpack = require('webpack');

const getPlugins = function(env) {
  const GLOBALS = {
    'process.env.NODE_ENV': JSON.stringify(env),
    __DEV__: env == 'development'
  };

  const plugins = [
    new webpack.DefinePlugin(GLOBALS) //Passes variables to Webpack. https://facebook.github.io/react/downloads.html
  ];

      plugins.push(new webpack.HotModuleReplacementPlugin());
      plugins.push(new webpack.NoEmitOnErrorsPlugin());

  return plugins;
};

module.exports = {
  entry: ['webpack/hot/dev-server', 'eventsource-polyfill', './src/js/index.js'],
  plugins: getPlugins('development'),
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: ['babel-loader', 'eslint-loader']
      }
    ]
  },
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
    resolve: {
      alias: {
        'react': path.join(__dirname, 'node_modules', 'react')
      },
      extensions: ['.js', '.json', '.jsx']
    }
};