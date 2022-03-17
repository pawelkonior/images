export const retrieveData = async (endpoint, method = "GET", body = null) => {
  const response = await fetch(`/api/v1/${endpoint}`, {
    method,
    headers: {
      "Access-Control-Allow-Headers": "*",
      "Content-Type": "application/json",
    },
    body,
  });

  return await response.json();
};
