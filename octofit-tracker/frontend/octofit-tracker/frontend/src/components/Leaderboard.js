import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    console.log('Leaderboard API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching leaderboard:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="loading-container"><div className="spinner-border" role="status"></div></div>;
  if (error) return <div className="alert alert-danger"><strong>Error!</strong> {error}</div>;

  return (
    <div className="fade-in">
      <h2>🏆 Leaderboard</h2>
      <div className="table-responsive">
        <table className="table table-hover">
          <thead>
            <tr>
              <th>Rank</th>
              <th>User</th>
              <th>Score</th>
              <th>Activities</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.map((entry, index) => {
              const rank = index + 1;
              let rankClass = 'default';
              if (rank === 1) rankClass = 'gold';
              else if (rank === 2) rankClass = 'silver';
              else if (rank === 3) rankClass = 'bronze';
              
              return (
                <tr key={entry.id || index}>
                  <td>
                    <span className={`rank-badge ${rankClass}`}>{rank}</span>
                  </td>
                  <td><strong>{entry.user || entry.username}</strong></td>
                  <td><span className="badge bg-warning text-dark">{entry.score || entry.total_points} pts</span></td>
                  <td><span className="badge bg-info">{entry.activity_count || 0} activities</span></td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
      {leaderboard.length === 0 && (
        <div className="empty-state">
          <p className="text-muted">🏅 No leaderboard data available. Be the first to compete!</p>
        </div>
      )}
    </div>
  );
}

export default Leaderboard;
