vector<int> topologySortInit(graphNotWeighted &G) {
    int n = G.size();
    vector<int> resultOrder;
    vector<char> color(n, 'w');

    for (int v = 0; v < n; v++)
        if (color[v] == 'w')
            topologySortProc(G, v, color, resultOrder);
    reverse(resultOrder.begin(), resultOrder.end());
    return resultOrder;
}

void topologySortProc(graphNotWeighted &G, int start, vector<char> &color, vector<int> &order) {
    stack<pair<int, int> > S;

    S.push(make_pair(start, -1));
    color[start] = 'g';
    while (S.size()) {
        int v = S.top().first;
        int u = S.top().second;
        int w = -1;
        for (int i = 0; i < G[v].size(); i++)
            if (G[v][i] != u && color[G[v][i]] == 'w') {
                w = G[v][i];
                break;
            }
        if (w == -1) {
            S.pop();
            color[v] = 'b';
            order.push_back(v);
        }
        else {
            S.top().second = w;
            if (color[w] == 'w') {
                S.push(make_pair(w, -1));
                color[w] = 'g';
            }
        }
    }
    return;
}
