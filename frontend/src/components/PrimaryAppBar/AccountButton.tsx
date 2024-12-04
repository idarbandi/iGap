import { Box, IconButton, Menu, MenuItem } from "@mui/material";
import { AccountCircle } from "@mui/icons-material";
import DarkModeSwitch from "./DarkMode/DarkModeSwitch.tsx";
import { useState } from "react";

const AccountButton = () => {
  // State to manage the anchor element for the menu
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);

  // Determine if the menu is open based on the anchor element's state
  const isMenuOpen = Boolean(anchorEl);

  // Handler to open the profile menu
  const handleProfileMenuOpen = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };

  // Handler to close the profile menu
  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  // JSX to render the menu
  const renderMenu = (
    <Menu
      anchorEl={anchorEl}
      anchorOrigin={{ vertical: "bottom", horizontal: "right" }}
      open={isMenuOpen}
      keepMounted
      onClose={handleMenuClose}
    >
      <MenuItem>
        {/* Component to switch between dark and light modes */}
        <DarkModeSwitch />
      </MenuItem>
    </Menu>
  );

  return (
    <Box sx={{ display: { xs: "flex" } }}>
      {/* Icon button to open the profile menu */}
      <IconButton edge="end" color="inherit" onClick={handleProfileMenuOpen}>
        <AccountCircle />
      </IconButton>
      {/* Render the menu */}
      {renderMenu}
    </Box>
  );
};

export default AccountButton;
