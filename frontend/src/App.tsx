// import Home from './pages/Home';
// import {
//   createBrowserRouter,
//   createRoutesFromElements,
//   Route,
//   RouterProvider
// } from 'react-router-dom';

// const router = createBrowserRouter(
//   createRoutesFromElements(
//     <Route>
//       <Route path='/fine/' element={<Home/>} ></Route>
//     </Route>
//   )
// )

// const App = () => {
//   return
//     <RouterProvider router={router} />;
// };

// export default App;

import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from 'react-router-dom';
import Home from './pages/Home';

function App() {
  const [count, setCount] = useState(0);
  const router = createBrowserRouter( createRoutesFromElements(
    <Route>
      <Route path="/fine/" element={<Home />}></Route>
    </Route>
    ) )

  return (
    <>
    <RouterProvider router={router} />
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>count is {count}</button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">Click on the Vite and React logos to learn more</p>
    </>
  );
}

export default App;
