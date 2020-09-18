const query = `
{
  book(id: 1) {
    id
    title
    author {
      name
      books {
        title
        authorId
      }
    }
  }
  
  authors {
    name
    books {
      title
    }
  }
}
`;

function executeQuery() {
  fetch('http://localhost:8000', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query }),
  })
    .then(res => res.json())
    .then(res => {
      showMessage(res);
    });
}

function showMessage(res) {
  htmlResult = JSON.stringify(res, null, 2).replaceAll(" ", "&nbsp;").replaceAll("\n", "<br/>");
  document.getElementById("result").innerHTML = htmlResult;
}
