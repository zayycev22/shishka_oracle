import { makeStyles } from "@mui/styles";


export default makeStyles(theme => ({

    textFileName: {
        fontSize: 18,
        fontWeight: 400,
        fontFamily: "Roboto",
        lineHeight: 1,
    },

    container: {
        display: "flex",
        flexDirection: "column",
        justifyContent: "flex-start",
        alignItems: "center",
        marginTop: "10vh",
        borderRadius: "50px",
        background: "#181818",
        width: "50vw",
        height: "50vh",
        marginBottom: "10vh",
    },

    title: {
        fontStyle: "normal",
        fontWeight: 600,
        fontSize: 40,
        color: "#00F43A",
        fontFamily: "Nunito",
    },

    sendContainer: {
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "center"
    },

    fileNameContainer: {
        width: "30vw",
        height: "8vh",
        background: "#39393A",
        borderRadius: 20,
        display:"flex",
        flexDirection:"row",
        justifyContent: "center",
        alignItems: "center",
        fontFamily: 'Nunito',
        fontStyle: "normal",
        fontWeight: 400,
        fontSize: "24px",
        lineHeight: "33px",
        color: "#E6E6E6"
    },

}))

