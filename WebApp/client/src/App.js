import React from "react"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Footer from "./components/footer"
import LandingPage from "./components/LandingPage"
import NavBar from "./components/nav-bar"

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={
          <div className="Jumbotron">
            <NavBar />
            <LandingPage />
            <Footer />
          </div>
        } />
      </Routes>
    </BrowserRouter>
  )
}
