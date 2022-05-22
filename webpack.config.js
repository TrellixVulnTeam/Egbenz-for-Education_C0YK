const path = require('path')
const webpack = require('webpack')
const mode = "production" // production || development

module.exports = {
  mode,
  entry: './app-web/index.js',
	output: {
		filename: './bundle.js',
		path: path.resolve(__dirname, './dist') 
  },
  module:{
    rules:[
        {
          test:/\.css$/,
          use:['style-loader','css-loader']
        },{
          test:/\.(ttf|woff|otf|eot|woff2)$/,
          type:'asset/resource',
          generator:{
            filename: './assets/[hash:10].[ext]'
          }
        }
    ]
  },
  plugins:[
    new webpack.ProvidePlugin({
      Watcher: [path.resolve(__dirname, './app-web/js/tools/globals.js'), 'Watcher'],
      Dep: [path.resolve(__dirname, './app-web/js/tools/globals.js'), 'Dep'],
      reactive: [path.resolve(__dirname, './app-web/js/tools/globals.js'), 'reactive'],
    })
  ]
  
}