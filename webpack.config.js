const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');


module.exports = {
    plugins: [new MiniCssExtractPlugin({
        filename: '../css/main.css'
    })],
    module: {
        rules: [
            {
                test: /\.(s[ac]|c)ss$/i,
                use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"],
            }
        ],
    },
    mode: 'development',
    entry: './static/js/main.js',
    output: {
        path: path.resolve(__dirname, './static/js'),
        filename: 'bundle.js',
    },
    devtool: "source-map",
};