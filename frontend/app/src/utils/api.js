export const retrieveData = async (endpoint, method = "GET", body = null) => {
  const response = await fetch(`http://localhost:3000/${endpoint}`, {
    method,
    body,
  });

  return await response.json();
};
