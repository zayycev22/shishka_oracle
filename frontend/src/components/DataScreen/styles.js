import { makeStyles } from "@mui/styles";


export default makeStyles(theme => ({

  container: {
    background: "#181818",
    borderRadius: "50px",
    width: "58vw",
    marginTop: 50,
    marginBottom: 50,
    display: "flex",
    flexDirection:"column"
  },

  titleContainer: {
    marginLeft: 20,
    display: "flex",
    flexDirection: "row",
    justifyContent: "flex-start",
    alignItems: "center"
  },

  imgContainer: {
    marginTop: 20,
    marginBottom: 20,
    width: 30,
    height: 60,
    cursor: "pointer"
  }



}))

