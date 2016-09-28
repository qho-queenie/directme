  $('.dropdown-button').dropdown({
      inDuration: 300,
      outDuration: 225,
      constrain_width: false, // Does not change width of dropdown to that of the activator
      hover: true, // Activate on hover
      gutter: 0, // Spacing from edge
      belowOrigin: false, // Displays dropdown below the button
      alignment: 'left' // Displays dropdown with edge aligned to the left of button
    }
  );
        

(function(){
  var now, pics = {
    rain: 'http://i.imgur.com/VIKAkHF.jpg',
    perfect: 'http://i.imgur.com/TsmJjpn.jpg',
    hot: 'http://i.imgur.com/25bal3D.jpg',
    show: function(){
      return now > 5 && now < 12? this.rain : now > 11 && now < 19? this.perfect : this.hot;
    }
  };

  (function(){
    now = new Date().getHours();
    document.documentElement.style.backgroundImage = 'url(' + pics.show() + ')';
    if(typeof pics.interval === 'undefined'){
      pics.interval = setInterval(arguments.callee, 10000);
    }
  })();
})();

// // Set speed (milliseconds)
//   var speed = 3000

//   // Specify the image files
//   var Pic = new Array() // don't touch this
//   // to add more images, just continue
//   // the pattern, adding to the array below

//   Pic[0] = 'img_1.jpg'
//   Pic[1] = 'img_2.jpg'
//   Pic[2] = 'img_3.jpg'
//   Pic[3] = 'img_4.jpg'


//   var t
//   var j = 0
//   var p = Pic.length

//   var preLoad = new Array()
//   for (i = 0; i < p; i++){
//      preLoad[i] = new Image()
//      preLoad[i].src = Pic[i]
//   }

//   function runBGSlideShow(){
//      if (document.body){
//      document.body.background = Pic[j];
//      j = j + 1
//      if (j > (p-1)) j=0
//      t = setTimeout('runBGSlideShow()', speed)
//      }
//   }