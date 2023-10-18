function programmerStrings(s) {
  const targetString = "programmer";
  let leftmostIndex = -1;
  let rightmostIndex = -1;
  let count = 0;

  let startIndex = s.indexOf(targetString);
  let endIndex = s.lastIndexOf(targetString);

  if (startIndex !== -1 && endIndex !== -1 && startIndex < endIndex) {
    leftmostIndex = startIndex;
    rightmostIndex = endIndex + targetString.length - 1;
  }

  if (leftmostIndex !== -1 && rightmostIndex !== -1) {
    count = rightmostIndex - leftmostIndex - targetString.length + 1;
  }

  return count;
}

const result = programmerStrings("xprogxrmaxemrppprmmograeiruu");
console.log(result);
