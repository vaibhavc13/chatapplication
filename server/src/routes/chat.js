const express = require('express');
const router = express.Router();
const aiRouter = require('../services/aiRouter');

router.post('/', async (req, res) => {
    const { messages } = req.body;
    try {
        const result = await aiRouter.routeRequest(messages);
        res.json(result);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

module.exports = router;
