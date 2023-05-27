import './App.css';

function BookmarkTile(props) {
  return(
    <div style={{width: "100%", height: "5rem", display: "flex", justifyContent: "center", alignContent:"center", background: "#3333ff", borderRadius: "0.25rem", boxShadow: "1rem 1rem 0 0 #113", margin: "1rem"}}>
      {props.title}
    </div>
  )
}

function App() {
  return (
    <div className="App" style={{display: "flex", justifyContent: "center", flexDirection: "column"}}>
      <h1>Hello World</h1>

      My name is Riley and I hope this isn't broken.
      <div className="gridContainer" style={{display: "grid", justifyContent: "center", alignItems:"center", gridTemplateColumns:"1fr 1fr 1fr 1fr 1fr", gap: "4rem", marginTop: "4rem"}}>
        <BookmarkTile title="hello World!"></BookmarkTile>
        <BookmarkTile title="hello World!"></BookmarkTile>
        <BookmarkTile title="hello World!"></BookmarkTile>
        <BookmarkTile title="hello World!"></BookmarkTile>
      </div>
    </div>
  );
}

export default App;