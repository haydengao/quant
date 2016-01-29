(function() {
    var biz_path = require.toUrl('business') + '/js';
    require.config({
        paths: {
            'business/js/main': biz_path + '/main.4901a7b29833184454e7',
            'business/css/main': biz_path + '/../css/main.78d1255134d0efa598029735c5dfb275',

            mathjax: 'https://ylibs.wmcloud.com/mathjax/2.4/MathJax.js?config=TeX-AMS-MML_HTMLorMML'
        },
        shim: {
            mathjax: {
                exports: "MathJax"
            }
        }
    });
})();

window.getApp = function(app, url) {
    return window._preboot.appRoot + '/' + app + url;
};
window.getAppRoot = function(){
    return window._preboot.appRoot;
};

define([
    'achy',
    'css!yestrap-light',
    'css!fontawesome',
    'css!business/css/main'
], function() {
    return {
        init: function() {
            require([
                'achy/utils/head',
                'business/js/main'
            ]);
        }
    };
});
