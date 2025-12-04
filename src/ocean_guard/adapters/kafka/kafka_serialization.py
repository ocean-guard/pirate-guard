import confluent_kafka.serialization

KafkaMessage = confluent_kafka.Message

KafkaSerializer = confluent_kafka.serialization.Serializer
KafkaStringSerializer = confluent_kafka.serialization.StringSerializer

KafkaDeserializer = confluent_kafka.serialization.Deserializer
KafkaStringDeserializer = confluent_kafka.serialization.StringDeserializer
