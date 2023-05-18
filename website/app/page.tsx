import React from "react";
// title, src, alt, bg-color, fg-color, tags, id) {

function IsImg(props: { h1: string; alt: string; img: string }) {
  if (props.img) {
    return <img className="icon" src={props.img} alt={props.alt} />;
  } else {
    return <div className="icon">{props.h1}</div>;
  }
}

function BookmarkTile(props: {
  href: string;
  id: string;
  img: string;
  h1: string;
  alt: string;
  text: string;
}) {
  return (
    <a href={props.href} className="button" id={props.id}>
      <IsImg h1={props.h1} alt={props.alt} img={props.img} />
      <div className="text">{props.text}</div>
    </a>
  );
}

function BookmarksList(props: { n: number }) {
  const bookmarks = Array.from({ length: props.n }, (_, index) => ({
    href: "https://www.youtube.com/watch?v=__mSgDEOyv8",
    id: `bookmark-${index}`,
    img: "",
    h1: "😎",
    text: "Text",
    alt: "",
  }));

  return (
    <React.Fragment>
      {bookmarks.map((bookmark) => (
        <BookmarkTile
          key={bookmark.id}
          href={bookmark.href}
          id={bookmark.id}
          img={bookmark.img}
          h1={bookmark.h1}
          text={bookmark.text}
          alt={bookmark.alt}
        />
      ))}
    </React.Fragment>
  );
}

export default function Home() {
  return (
    <div className="container">
      <BookmarkTile
        href="https://www.youtube.com/watch?v=__mSgDEOyv8"
        id="191241hfds"
        img=""
        h1="Click Me!"
        text="Text to be displayed"
        alt=""
      />
      <BookmarkTile
        href="https://www.youtube.com/watch?v=__mSgDEOyv8"
        id="191241hfds"
        img=""
        h1="Click Me!"
        text="Text to be displayed"
        alt=""
      />
      <BookmarksList n={12} />
    </div>
  );
}
