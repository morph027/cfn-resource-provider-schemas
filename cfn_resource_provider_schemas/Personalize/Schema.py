SCHEMA = {
  "typeName" : "AWS::Personalize::Schema",
  "description" : "Resource schema for AWS::Personalize::Schema.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-personalize",
  "properties" : {
    "Name" : {
      "description" : "Name for the schema.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 63,
      "pattern" : "^[a-zA-Z0-9][a-zA-Z0-9\\-_]*"
    },
    "SchemaArn" : {
      "description" : "Arn for the schema.",
      "type" : "string",
      "maxLength" : 256,
      "pattern" : "arn:([a-z\\d-]+):personalize:.*:.*:.+"
    },
    "Schema" : {
      "description" : "A schema in Avro JSON format.",
      "type" : "string",
      "maxLength" : 10000
    },
    "Domain" : {
      "description" : "The domain of a Domain dataset group.",
      "type" : "string",
      "enum" : [ "ECOMMERCE", "VIDEO_ON_DEMAND" ]
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name", "Schema" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Schema", "/properties/Domain" ],
  "readOnlyProperties" : [ "/properties/SchemaArn" ],
  "primaryIdentifier" : [ "/properties/SchemaArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "personalize:CreateSchema", "personalize:DescribeSchema" ]
    },
    "read" : {
      "permissions" : [ "personalize:DescribeSchema" ]
    },
    "delete" : {
      "permissions" : [ "personalize:DeleteSchema", "personalize:DescribeSchema" ]
    },
    "list" : {
      "permissions" : [ "personalize:ListSchemas" ]
    }
  }
}