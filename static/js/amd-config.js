define({
    paths: {
        //Path
        lib: 'lib',
        plugin: 'plugin',
        compressed: 'compressed',
        src: 'src',
        achilles: '..',

        common: '../business/common',

        bootstrap: 'lib/bootstrap',
        bootstrapjs: 'lib/bootstrap/js/bootstrap',
        'yestrap': '../css/yestrap',
        'yestrap-light': '../css/yestrap-light',
'yestrap-light': '../css/yestrap-light.8e2a1ea4',
'yestrap': '../css/yestrap.c4a0c177',

        //Lib
        jquery: 'lib/jquery-1.8.1.min',
        easyui: 'lib/jquery.easyui-1.3.3_c2.min',
        ext: 'lib/ext-all',
        backbone: 'lib/backbone-1.0.0.min',
        lodash: 'lib/lodash.min',
        underscore: 'lib/lodash.underscore.min',
        jqueryui: 'lib/jquery.ui-1.10.3.min',
        d3: 'lib/d3/d3.min',
        angular: 'lib/angular.min',

        //css
        fontawesome: '../css/font-awesome.min',

        //Plugin
        text: "plugin/text",
        tpl: 'plugin/tpl',
        css: 'plugin/css',
        es6: 'plugin/es6',
        babel: 'plugin/babel',
        es6poly: 'plugin/es6poly',
        caret: 'plugin/jquery.caret',
        atwho: 'plugin/jquery.atwho',
        mustache: 'plugin/mustache',
        amcharts: 'plugin/amcharts',
        highcharts: 'plugin/highstock/highstock',
        highcharts_exporting: 'plugin/highstock/exporting',
        atmosphere: "plugin/atmosphere-2.0",
        percent: "plugin/percent/percent",
        portal: "plugin/easyui.portlet/jquery.portal",
        autocomplete: "plugin/jquery-ui-autocomplete/js/jquery-ui-1.10.3.custom.min",
        dragdrop: "plugin/jquery-ui-autocomplete/js/jquery-ui-1.10.3.custom.min",
        timepicker: "plugin/bootstrap-timepicker.min",
        datepicker: "plugin/bootstrap-datepicker",
        tagit: 'plugin/tag-it.min',
        //mousewheel: 'plugin/perfect-scrollbar-0.4.6.with-mousewheel.min',
        //scrollbar: 'plugin/perfect-scrollbar-0.4.6.min',
        ueditor_config: 'plugin/ueditor/ueditor.config',
        ueditor_lang: 'plugin/ueditor/lang/zh-cn/zh-cn',
        ueditor: 'plugin/ueditor/ueditor.all.min',
        peity: 'plugin/jquery.peity',
        datatables: 'plugin/jquery.dataTables.min',
        datatables_scroller: 'plugin/dataTables.scroller.min',
        'datatables-fixedheader': 'plugin/dataTables.fixedHeader.min',
        qtip: 'plugin/jquery.qtip.min',
        uiRouter: 'plugin/angular-ui-router.min',

        //CC
        cc: 'compressed/cc-1.1.0',

        //machy
        machy: '../machy.6ea440e0',

        //achy
        achy: '../achy.a75bf2ee',
'achy/biz/yauth': '../achy/biz/yauth.da19a455',
'achy/biz/im': '../achy/biz/im.731073e1',
'achy/biz/ie': '../achy/biz/ie.6717bba9',
'achy/biz/globalFooter': '../achy/biz/globalFooter.0a64eb53',
'achy/biz/globalBar2': '../achy/biz/globalBar2.35fbfa4c',
'achy/biz/globalBar': '../achy/biz/globalBar.ce478519',
'achy/biz/feedback': '../achy/biz/feedback.dc28dae1',
'achy/biz/auth': '../achy/biz/auth.9cf57630',
'achy/biz/yauth/style': '../achy/biz/yauth/style.5c97a3af',
'achy/biz/myDock/style': '../achy/biz/myDock/style.00000000',
'achy/biz/im/style': '../achy/biz/im/style.a4bc6bbd',
'achy/biz/globalFooter/style': '../achy/biz/globalFooter/style.6b7f2e0e',
'achy/biz/globalBar2/style': '../achy/biz/globalBar2/style.ccde8427',
'achy/biz/globalBar/style': '../achy/biz/globalBar/style.a3d5c2fe',
'achy/biz/feedback/style': '../achy/biz/feedback/style.094de7fc',
'achy/biz/auth/style': '../achy/biz/auth/style.32bec323',

        //Code Editor
        codemirror: 'plugin/codemirror-4.1/codemirror',
        jseditor: 'plugin/codemirror-4.1/javascript',

        i18n: 'compressed/i18n/'
    },
    shim: {
        'backbone': {
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
        },
        'underscore': {
            exports: '_'
        },
        'device': {
            exports: 'device'
        },
        'mustache': {
            exports: 'Mustache'
        },
        'easyui': {
            deps: ['jquery']
        },
        'cc': {
            deps: ['jquery', 'easyui']
        },
        'atwho': {
            deps: ['jquery', 'caret']
        },
        'highcharts_exporting': {
            deps: ['highcharts']
        },
        'autocomplete': {
            deps: ['jquery']
        },
        'dragdrop': {
            deps: ['jquery']
        },
        'peity': {
            deps: ['jquery']
        },
        'tagit': {
            deps: ['autocomplete']
        },
        'ueditor_config': {

        },
        'ueditor': {
            deps: ['ueditor_config'],
            exports: 'UE'
        },
        'datatables_scroller': {
            deps: ['datatables']
        },
        'uiRouter': {
            deps: ['angular']
        },
        'bootstrapjs': {
            deps: ['jquery']
        },
        'codemirror': {
            exports: 'CodeMirror'
        },
        'jseditor': {
            deps: ['codemirror']
        }
    },
    config: {
        text: {
            useXhr: function(url, protocol, hostname, port) {
                return true;
            }
        }
    }
});
