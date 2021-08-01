const state = {
  article: {},
  articles: [],
  articles_count: 0,
  itemsPerPage: 10,
  comments: [],
  errors: {},
  is_authenticated: false,
  is_loading: false,
  profile: {
    created_on: null,
    email: null,
    id: null,
    last_login: null,
    password: null,
    username: null,
    image: null,
  },
  tags: [],
  user: {
    created_on: null,
    email: null,
    id: null,
    last_login: null,
    password: null,
    username: null,
    image: null,
  },
};

const getters = {
  article() {
    return state.article;
  },

  articles() {
    return state.articles;
  },

  articles_count() {
    return state.articles_count;
  },
  pages() {
    if (state.articles_count <= state.itemsPerPage) {
      return [];
    }
    return [
      ...Array(Math.ceil(state.articles_count / state.itemsPerPage)).keys()
    ].map(e => e + 1);
  },
  comments() {
    return state.comments;
  },

  errors() {
    return state.errors;
  },

  is_authenticated() {
    return state.is_authenticated;
  },

  is_loading() {
    return state.is_loading;
  },

  profile() {
    return state.profile;
  },

  tags() {
    return state.tags;
  },

  user() {
    return state.user;
  },
};

export { getters, state };
