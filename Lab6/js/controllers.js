var portfolioApp = angular.module('portfolioApp',[]);

portfolioApp.controller('GalleryListCtrl', function($scope)
{
    $scope.galleries = 
    [
        { 'title':'AUDI SQ5',
        'when':'03-06-2018',
        'thumbnailUrl':'img/Z1.jpg'
        },
        { 'title':'BMW M4',
        'when':'06-08-2021',
        'thumbnailUrl':'img/Z2.png'
        },
        { 'title':'911 Carrera 4 GTS ',
        'when':'01-02-2022',
        'thumbnailUrl':'img/Z3.jpeg'
        },
        { 'title':'Hyundai Bayon',
        'when':'19-01-2022',
        'thumbnailUrl':'img/Z4.jpeg'
        },
        { 'title':'Lexus IS',
        'when':'25-04-2019',
        'thumbnailUrl':'img/Z5.jpg'
        },
        { 'title':'KIA RIO',
        'when':'13-07-2017',
        'thumbnailUrl':'img/Z6.jpg'
        }
    ];
    $scope.galleries.length;
});