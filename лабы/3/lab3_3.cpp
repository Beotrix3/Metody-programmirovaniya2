graphNotWeighted transposingGraph(graphNotWeighted &G) {
    int n = G.size();
    graphNotWeighted GT(n);

    vector<int> count(n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < G[i].size(); j++)
            count[G[i][j]]++;

    for (int i = 0; i < n; i++)
        GT[i].reserve(count[i]);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < G[i].size(); j++)
            GT[G[i][j]].push_back(i);
    return GT;
}
graphNotWeighted getComponent(graphNotWeighted &G, int start, vector<char> &color) {
    stack<pair<int, int> > S;
    graphNotWeighted component(G.size());

    bool isEmpty = false;
    for(int p = 0; p < G[start].size(); p++)
        if(color[G[start][p]] == 'w')
            isEmpty = true;

    if(isEmpty == false) {
        component[start].push_back(start);
        color[start] = 'b';
        return component;
    }
    S.push(make_pair(start, -1));
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
        }
        else {
            S.top().second = w;
            if (color[w] == 'w') {
                component[w].push_back(v);
                S.push(make_pair(w, -1));
                color[w] = 'g';
            }
        }
    }
    return component;
}

vector<graphNotWeighted> strongConnectedComponents(graphNotWeighted &G) {
    int n = G.size();
    vector<int> order = topologySortInit(G);
    graphNotWeighted GT = transposingGraph(G);
    vector<graphNotWeighted> strongConnectedComponents;
    vector<char> color(n, 'w');
    for (int i = 0; i < n; i++)
        if (color[order[i]] == 'w')
            strongConnectedComponents.push_back(getComponent(GT, order[i], color));
    return strongConnectedComponents;
}
