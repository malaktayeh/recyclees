import React from 'react';
import HeroImg from './../assets/home-background.jpg'
import injectSheet from 'react-jss';

const styles = {
    thumbnail: {
      position: 'relative',
  },
  caption: {
      color: 'white',
      position: 'absolute',
      top: '35%',
      left: 0,
      width: '100%',
      textAlign: 'center',
      fontSize: '2rem',
      fontWeight: 'bold'
  },
  shadow: {
    textShadow: '0 0 3px black' 
  }
}

const Hero = ({classes}) => (
    <div className={classes.thumbnail}>
        <img src={HeroImg} className="img-fluid" alt="Collection of old TVs" /> 
        <div className={classes.caption}>
            <p className={classes.shadow}>Donate unwanted electronic devices!</p>
        </div>
    </div>
);

export default injectSheet(styles)(Hero);
