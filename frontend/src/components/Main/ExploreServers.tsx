import {
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Box,
  Typography,
} from "@mui/material";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Grid from "@mui/material/Grid";
import Container from "@mui/material/Container";
import ListItemAvatar from "@mui/material/ListItemAvatar";
import Avatar from "@mui/material/Avatar";
import { useParams } from "react-router-dom";
import useCrud from "../../hooks/useCrud.ts";
import { useEffect } from "react";
import { MEDIA_URL } from "../../config.ts";
import { Link } from "react-router-dom";

/**
 * Interface representing a server.
 */
interface Server {
  id: number;           // Unique identifier for the server
  name: string;         // Name of the server
  description: string;  // Description of the server
  icon: string;         // URL to the server's icon
  category: string;     // Category the server belongs to
  banner: string;       // URL to the server's banner image
}

/**
 * Component to explore servers based on category.
 *
 * Uses URL parameters to determine the category and fetches server data accordingly.
 *
 * @returns {JSX.Element} The ExploreServers component.
 */
const ExploreServers = (): JSX.Element => {
  // Extract category name from URL parameters
  const { categoryName } = useParams();
  
  // Construct URL based on category name
  const url = categoryName
    ? `/server/?category=${categoryName}`
    : "/server/";
  
  // Custom hook to handle CRUD operations and data fetching
  const { dataCRUD, fetchData } = useCrud<Server>([], url);

  // Fetch data whenever categoryName changes
  useEffect(() => {
    fetchData();
  }, [categoryName]);

  // Add your JSX here to render the server data
  return (
    // Example: Render the server names
    <div>
      {dataCRUD.map((server) => (
        <div key={server.id}>{server.name}</div>
      ))}
    </div>
  );
}

export default ExploreServers;

  return (
    <>
      <Container maxWidth="lg">
        <Box sx={{ pt: 6 }}>
          <Typography
            variant="h3"
            noWrap
            component="h1"
            sx={{
              display: {
                sm: "block",
                fontWeight: 700,
                letterSpacing: "-2px",
                textTransform: "capitalize",
              },
              textAlign: { xs: "center", sm: "left" },
            }}
          >
            {categoryName ? categoryName : "Popular Channels"}
          </Typography>
        </Box>
        <Box>
          <Typography
            variant="h6"
            noWrap
            component="h2"
            color="textSecondary"
            sx={{
              display: {
                sm: "block",
                fontWeight: 700,
                letterSpacing: "-1px",
              },
              textAlign: { xs: "center", sm: "left" },
            }}
          >
            {categoryName
              ? `Channels talking about ${categoryName}`
              : "Check out some of our popular channels"}
          </Typography>
        </Box>

        <Typography
          variant="h6"
          sx={{ pt: 6, pb: 1, fontWeight: 700, letterSpacing: "-1px" }}
        >
          Recommended Channels
        </Typography>
        <Grid container spacing={{ xs: 0, sm: 2 }}>
          {dataCRUD.map((item) => (
            <Grid item key={item.id} xs={12} sm={6} md={6} lg={3}>
              <Card
                sx={{
                  height: "100%",
                  display: "flex",
                  flexDirection: "column",
                  boxShadow: "none",
                  backgroundImage: "none",
                  borderRadius: 0,
                }}
              >
                <Link
                  to={`/server/${item.id}`}
                  style={{ textDecoration: "none", color: "inherit" }}
                >
                  <CardMedia
                    component="img"
                    image={
                      item.banner
                        ? `${MEDIA_URL}${item.banner}`
                        : "https://source.unsplash.com/random/"
                    }
                    alt="random"
                    sx={{ display: { xs: "none", sm: "block" } }}
                  />
                  <CardContent
                    sx={{
                      flexGrow: 1,
                      p: 0,
                      "&:last-child": { paddingBottom: 0 },
                    }}
                  >
                    <List>
                      <ListItem disablePadding>
                        <ListItemIcon sx={{ minWidth: 0 }}>
                          <ListItemAvatar sx={{ minWidth: "50px" }}>
                            <Avatar
                              alt="server Icon"
                              src={`${MEDIA_URL}${item.icon}`}
                            />
                          </ListItemAvatar>
                        </ListItemIcon>
                        <ListItemText
                          primary={
                            <Typography
                              variant="body2"
                              textAlign="start"
                              sx={{
                                textOverflow: "ellipsis",
                                overflow: "hidden",
                                whiteSpace: "nowrap",
                                fontWeight: 700,
                              }}
                            >
                              {item.name}
                            </Typography>
                          }
                          secondary={
                            <Typography variant="body2">
                              {item.category}
                            </Typography>
                          }
                        />
                      </ListItem>
                    </List>
                  </CardContent>
                </Link>
              </Card>
            </Grid>
          ))}
        </Grid>
      </Container>
    </>
  );
};

export default ExploreServers;
