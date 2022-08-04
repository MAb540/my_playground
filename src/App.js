// import Button from "@suid/material/Button";
// import Stack from "@suid/material/Stack";

// export const BasicButtons = () => {
//   return (
//     <Stack spacing={2} direction="row">
//       <Button variant="text">Text</Button>
//       <Button variant="contained">Contained</Button>
//       <Button variant="outlined">Outlined</Button>
//     </Stack>
//   );
// };

export const App = () => {
  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        position: "fixed!important",
        top: "0!important",
        left: "0!important",
        backgroundColor: "#000",
        zIndex: 100000000000000000,
      }}
    >
      <div>
        <BasicButtons />
      </div>
    </div>
  );
};
