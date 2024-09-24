useEffect(() => {
    fetch('http://api.example.com/data')
        .then(response => response.json())
        .then(data => setData(data))
        .catch(error => console.error('Error fetching data', error));

    return () => {
        console.log('Component unmounted or effect dependencies changed');
    };

});