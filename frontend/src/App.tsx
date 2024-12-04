/**
 * این کامنت‌ها و داک‌استرینگ‌ها توسط من، Idarbandi، اضافه شده‌اند.
 * برای پشتیبانی بیشتر لطفاً با من تماس بگیرید: darbandidr99@gmail.com
 * GitHub: https://github.com/idarbandi/
 */

import Home from "./pages/Home.tsx";
import Server from "./pages/Server.tsx";
import Explore from "./pages/Explore.tsx";
import { Route, Routes, BrowserRouter } from "react-router-dom";
import ToggleColorMode from "./components/ToggleColorMode.tsx";
import Login from "./pages/Login.tsx";
import { AuthServiceProvider } from "./context/AuthContext.tsx";
import TestLogin from "./pages/TestLogin.tsx";
import ProtectedRoute from "./services/ProtectedRoute.tsx";
import Register from "./pages/Register.tsx";

/**
 * کامپوننت اصلی اپلیکیشن.
 * شامل مسیرها (routes)، ارائه دهنده خدمات احراز هویت (AuthServiceProvider) و قابلیت تغییر حالت رنگ (ToggleColorMode).
 *
 * @returns {JSX.Element} کامپوننت اصلی اپلیکیشن.
 */
const App = (): JSX.Element => {
  return (
    <BrowserRouter>
      <AuthServiceProvider>
        <ToggleColorMode>
          <Routes>
            {/* مسیر خانه */}
            <Route path="/" element={<Home />} />

            {/* مسیر سرور با مسیریابی محافظت‌شده */}
            <Route
              path="/server/:serverId/:channelId?"
              element={
                <ProtectedRoute>
                  <Server />
                </ProtectedRoute>
              }
            />

            {/* مسیر اکتشاف */}
            <Route path="/explore/:categoryName" element={<Explore />} />

            {/* مسیر ورود */}
            <Route path="/login" element={<Login />} />

            {/* مسیر ثبت نام */}
            <Route path="/register" element={<Register />} />

            {/* مسیر ورود آزمایشی با مسیریابی محافظت‌شده */}
            <Route
              path="/testlogin"
              element={
                <ProtectedRoute>
                  <TestLogin />
                </ProtectedRoute>
              }
            />
          </Routes>
        </ToggleColorMode>
      </AuthServiceProvider>
    </BrowserRouter>
  );
};

export default App;
