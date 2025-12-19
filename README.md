# vitals-producer-anomaly-97

This project generates random vitals data with occasional anomalies and sends it to a Kafka topic.

## Usage

1.  Clone the repository:

    ```bash
    git clone https://github.com/Gautam0610/vitals-producer-anomaly-97.git
    cd vitals-producer-anomaly-97
    ```
2.  Set up your `.env` file with the required Kafka configuration (see `.env.example`).
3.  Build the Docker image:

    ```bash
    docker build -t vitals-producer .
    ```
4.  Run the Docker container:

    ```bash
    docker run -d vitals-producer
    ```

## Configuration

The following environment variables must be set in the `.env` file:

*   `OUTPUT_TOPIC`: The Kafka topic to send vitals data to.
*   `BOOTSTRAP_SERVERS`: The Kafka bootstrap servers.
*   `SASL_USERNAME`: The SASL username for Kafka authentication.
*   `SASL_PASSWORD`: The SASL password for Kafka authentication.
*   `SECURITY_PROTOCOL`: The security protocol for Kafka (e.g., `SASL_SSL`).
*   `SASL_MECHANISM`: The SASL mechanism for Kafka (e.g., `PLAIN`).
*   `INTERVAL_MS`: The interval in milliseconds between sending data points.

## Example .env file

```
OUTPUT_TOPIC=vitals-topic
BOOTSTRAP_SERVERS=kafka-broker1:9092,kafka-broker2:9092
SASL_USERNAME=your_username
SASL_PASSWORD=your_password
SECURITY_PROTOCOL=SASL_SSL
SASL_MECHANISM=PLAIN
INTERVAL_MS=1000
```