console.log("Bokeh Loaded")
import { Bokeh1Background } from 'https://cdn.jsdelivr.net/npm/threejs-components@0.0.2/build/backgrounds/bokeh1.cdn.min.js';

const bokeh1Background = Bokeh1Background(document.getElementById('webgl-canvas'));
bokeh1Background.loadMap('https://cdn.jsdelivr.net/npm/threejs-components@0.0.2/build/assets/bokeh-particles2.png');
bokeh1Background.setColors([0xf83090, 0xd908c0, 0xb4c276]);

