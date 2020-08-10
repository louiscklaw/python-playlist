import React from 'react'

import style from '../scss/style.module.scss'

import {combineStyle} from '../../utils/common'

function Card(props){
  return(

    <div className={style.card}>

      {/* card-image */}
      <div className={style.cardImage}>
        <figure className={style.is4by3} style={{textAlign:'center'}}>
          <div id="canvas-holder" style={{width: '90%', margin: 'auto'}}>
            <canvas id="chart-area-unit-test"></canvas>
          </div>
        </figure>
      </div>
      {/* card-image */}

      {/* card-content */}
      <div className={style.cardContent}>
        {/* media */}
        <div className={style.media}>
          {/* media-content */}
          <div className={style.mediaContent}>
            <p className={combineStyle([style.title, style.is4])}>
              Unit test
            </p>

          </div>
          {/* media-content */}
        </div>
        {/* media */}


        {/* content */}
        <div className={style.content}>
          <p>
            unit test content
          </p>
          <table className={style.table} style={{fontSize: 'small'}}>
            <thead>
              <tr>
                <td>Passed</td>
                <td>Failed</td>
                <td>In progress</td>
                <td>Error</td>
              </tr>
              <tr>
                <td>10</td>
                <td>2</td>
                <td>13</td>
                <td>1</td>
              </tr>
            </thead>
          </table>
        </div>
        {/* content */}


      </div>
      {/* card-content */}


    </div>

  )
}

export default Card