import React from 'react'

import style from '../scss/style.module.scss'

function Card(props){
  return(

    <div className={style.card}>
      <header className={style['card-header']}>
        <h3 className={style['card-header-title']}>TestStringMethods1</h3>
      </header>

      <div className={style['result-tile']}>
        <div className={style['result-grid-wrapper']}>
          <div class="box1">P</div>
          <div class="box2">E</div>
          <div class="box3">S</div>
          <div class="box4">F</div>
        </div>
      </div>

      <div className={style['card-content']}>
        <div className={style['media']}>
          <div className={style['media-content']}>

          </div>
        </div>

        <div className={style['content']}>
          testing the outlook of the page
          <br /><a>@bulmaio</a>.
          <br /><a href="#">#css</a>
          <br /><a href="#">#responsive</a>
          <br />
          <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
        </div>

      </div>
    </div>

  )
}

export default Card
