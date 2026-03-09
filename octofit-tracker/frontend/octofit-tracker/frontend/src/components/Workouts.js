import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Workouts API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="loading-container"><div className="spinner-border" role="status"></div></div>;
  if (error) return <div className="alert alert-danger"><strong>Error!</strong> {error}</div>;

  return (
    <div className="fade-in">
      <h2>💪 Workout Suggestions</h2>
      <div className="row">
        {workouts.map(workout => {
          const difficulty = workout.difficulty || 'Medium';
          let difficultyBadge = 'bg-info';
          if (difficulty === 'Easy') difficultyBadge = 'bg-success';
          else if (difficulty === 'Hard') difficultyBadge = 'bg-danger';
          
          return (
            <div key={workout.id} className="col-md-6 mb-4">
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">🏋️ {workout.name || workout.title}</h5>
                  <p className="card-text">{workout.description}</p>
                  <div className="d-flex justify-content-between align-items-center mt-3">
                    <div>
                      <span className="badge bg-primary me-2">⏱️ {workout.duration} min</span>
                      <span className={`badge ${difficultyBadge}`}>{difficulty}</span>
                    </div>
                    <button className="btn btn-sm btn-success">Start Workout</button>
                  </div>
                </div>
              </div>
            </div>
          );
        })}
      </div>
      {workouts.length === 0 && (
        <div className="empty-state">
          <p className="text-muted">💪 No workout suggestions available. Check back later for new routines!</p>
        </div>
      )}
    </div>
  );
}

export default Workouts;
