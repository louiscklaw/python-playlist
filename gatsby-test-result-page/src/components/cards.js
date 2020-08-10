import React from 'react'

import Card from './card'

import style from '../scss/style.module.scss'

function Cards(props){
  return(
    <div className={style.cardWrapper}>
      <Card />
      <Card />
      <Card />
      <Card />
    </div>
  )
}

export default Cards