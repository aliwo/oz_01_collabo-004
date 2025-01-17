import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Headerbar from "./Component/Header/index.jsx";
import Footer from "./Component/footer/index.jsx";
import Login from "./Page/Loginpage/index.jsx";
import MyPage from "./Page/MyPage/index.jsx";
import PetHouse from "./Page/PetHousePage/index.js";
import PetRestaurant from "./Page/PetRestauntPage/index.js";
import PetShop from "./Page/PetShopPage/index.jsx";
import Service from "./Page/SevicePage/index.jsx";
import SignupForm from "./Page/SignUpPage/index.jsx";
import Travel from "./Page/TravelPage/index.js";
import Home from "./Page/mainpage/index.jsx";

function App() {
  return (
    <BrowserRouter>
      <Headerbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/petshop" element={<PetShop />} />
        <Route path="/pethouse" element={<PetHouse />} />
        <Route path="/petrestaurant" element={<PetRestaurant />} />
        <Route path="/travel" element={<Travel />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignupForm />} />
        <Route path="mypage" element={<MyPage />} />
        <Route path="/service" element={<Service />} />
        <Route path="*" element={<h2>Page Not Found</h2>} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
