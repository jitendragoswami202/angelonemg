exports.handler = async (event, context) => {
    console.log("Webhook received:", event.body);
    return {
        statusCode: 200,
        body: JSON.stringify({ message: "Webhook received" }),
    };
};
