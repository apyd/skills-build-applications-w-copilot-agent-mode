import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
    console.log('Teams API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching teams:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="loading-container"><div className="spinner-border" role="status"></div></div>;
  if (error) return <div className="alert alert-danger"><strong>Error!</strong> {error}</div>;

  return (
    <div className="fade-in">
      <h2>👥 Teams</h2>
      <div className="row">
        {teams.map(team => (
          <div key={team.id} className="col-md-4 mb-4">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">🏢 {team.name}</h5>
                <p className="card-text">{team.description}</p>
                <div className="d-flex justify-content-between align-items-center mt-3">
                  <span className="badge bg-primary">{team.member_count || team.members?.length || 0} Members</span>
                  <button className="btn btn-sm btn-outline-primary">Join Team</button>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
      {teams.length === 0 && (
        <div className="empty-state">
          <p className="text-muted">🤝 No teams found. Create your first team to get started!</p>
        </div>
      )}
    </div>
  );
}

export default Teams;
