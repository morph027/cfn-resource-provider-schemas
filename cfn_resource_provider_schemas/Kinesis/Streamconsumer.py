SCHEMA = {
  "typeName" : "AWS::Kinesis::StreamConsumer",
  "description" : "Resource Type definition for AWS::Kinesis::StreamConsumer",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "ConsumerCreationTimestamp" : {
      "type" : "string"
    },
    "ConsumerName" : {
      "type" : "string"
    },
    "ConsumerARN" : {
      "type" : "string"
    },
    "ConsumerStatus" : {
      "type" : "string"
    },
    "StreamARN" : {
      "type" : "string"
    }
  },
  "required" : [ "ConsumerName", "StreamARN" ],
  "readOnlyProperties" : [ "/properties/ConsumerStatus", "/properties/ConsumerARN", "/properties/ConsumerCreationTimestamp", "/properties/Id" ],
  "createOnlyProperties" : [ "/properties/ConsumerName", "/properties/StreamARN" ],
  "primaryIdentifier" : [ "/properties/Id" ]
}