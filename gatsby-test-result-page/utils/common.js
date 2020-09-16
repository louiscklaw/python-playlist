
function helloUtil(){
  return 'helloUtil'
}

function combineStyle(styles_in){
  return styles_in.join(' ')
}

const combineStyles = combineStyle


function chunkArray(myArray, chunk_size){
  var index = 0;
  var arrayLength = myArray.length;
  var tempArray = [];

  for (index = 0; index < arrayLength; index += chunk_size) {
      let myChunk = myArray.slice(index, index+chunk_size);
      // Do something if you want with the group
      tempArray.push(myChunk);
  }

  return tempArray;
}

function fillToTheNearestRow(array_in, num_per_row){
  let row_ceil = Math.ceil(array_in.length/ num_per_row)
  let output_array_length = row_ceil * num_per_row

  while (array_in.length < output_array_length){
    array_in.push(null)
  }
  return array_in
}

export {
  combineStyle, combineStyles,
  helloUtil,
  chunkArray,
  fillToTheNearestRow
}