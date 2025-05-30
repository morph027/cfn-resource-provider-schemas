SCHEMA = {
  "typeName" : "AWS::CloudFormation::PublicTypeVersion",
  "description" : "Test and Publish a resource that has been registered in the CloudFormation Registry.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-cloudformation",
  "properties" : {
    "Arn" : {
      "description" : "The Amazon Resource Number (ARN) of the extension.",
      "pattern" : "arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:[0-9]{12}:type/.+",
      "type" : "string"
    },
    "TypeVersionArn" : {
      "description" : "The Amazon Resource Number (ARN) of the extension with the versionId.",
      "pattern" : "arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:[0-9]{12}:type/.+",
      "type" : "string"
    },
    "PublicVersionNumber" : {
      "description" : "The version number of a public third-party extension",
      "type" : "string",
      "minLength" : 5,
      "maxLength" : 64
    },
    "PublisherId" : {
      "description" : "The reserved publisher id for this type, or the publisher id assigned by CloudFormation for publishing in this region.",
      "pattern" : "[0-9a-zA-Z-]{1,40}",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 40
    },
    "PublicTypeArn" : {
      "description" : "The Amazon Resource Number (ARN) assigned to the public extension upon publication",
      "pattern" : "arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/.+",
      "type" : "string",
      "maxLength" : 1024
    },
    "TypeName" : {
      "description" : "The name of the type being registered.\n\nWe recommend that type names adhere to the following pattern: company_or_organization::service::type.",
      "pattern" : "[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}",
      "type" : "string"
    },
    "LogDeliveryBucket" : {
      "description" : "A url to the S3 bucket where logs for the testType run will be available",
      "type" : "string"
    },
    "Type" : {
      "description" : "The kind of extension",
      "enum" : [ "RESOURCE", "MODULE", "HOOK" ],
      "type" : "string"
    }
  },
  "oneOf" : [ {
    "required" : [ "TypeName", "Type" ]
  }, {
    "required" : [ "Arn" ]
  } ],
  "readOnlyProperties" : [ "/properties/PublicTypeArn", "/properties/TypeVersionArn", "/properties/PublisherId" ],
  "writeOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/LogDeliveryBucket", "/properties/PublicVersionNumber", "/properties/TypeName", "/properties/Type", "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/PublicTypeArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "cloudformation:TestType", "cloudformation:DescribeType", "cloudformation:PublishType", "cloudformation:DescribePublisher", "s3:GetObject", "s3:PutObject" ],
      "timeoutInMinutes" : 2160
    },
    "delete" : {
      "permissions" : [ ]
    },
    "read" : {
      "permissions" : [ "cloudformation:DescribeType", "cloudformation:DescribePublisher" ]
    },
    "list" : {
      "permissions" : [ "cloudformation:ListTypes" ]
    }
  },
  "additionalProperties" : False
}