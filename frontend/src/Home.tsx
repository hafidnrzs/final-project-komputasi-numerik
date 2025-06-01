import React from "react";

const Home = (props: React.HTMLAttributes<HTMLDivElement>) => {
  return (
    <div {...props}>
      <h1>Home Page</h1>
      <p>Welcome to the Home Page!</p>
    </div>
  );
};

export default Home;
