var portfolioApp = angular.module('portfolioApp',[]);

portfolioApp.controller('GalleryListCtrl', function($scope)
{
    $scope.galleries = 
    [
        { 'title':'AUDI SQ5',
        'when':'2018-03-03',
        'thumbnailUrl':'img/Z1.jpg'
        },
        { 'title':'BMW M4',
        'when':'2021-08-03',
        'thumbnailUrl':'img/Z2.png'
        },
        { 'title':'911 Carrera 4 GTS ',
        'when':'2022-01-02',
        'thumbnailUrl':'img/Z3.jpeg'
        },
        { 'title':'Hyundai Bayon',
        'when':'2022-01-19',
        'thumbnailUrl':'img/Z4.jpeg'
        },
        { 'title':'Lexus IS',
        'when':'2019-04-25',
        'thumbnailUrl':'img/Z5.jpg'
        },
        { 'title':'KIA RIO',
        'when':'2017-07-13',
        'thumbnailUrl':'img/Z6.jpg'
        }
    ];
    $scope.sortList = 
    [
        {
            'label':'Poukładane alfabetycznie',
            'value':'title'
        },
        {
            'label':'Poukładane chronologicznie od najstarszego do najnowszego samochodu',
            'value':'when'
        },
        {
            'label':'Od najnowszego do starszego samochodu',
            'value':'-when'
        },
    ];
    
});