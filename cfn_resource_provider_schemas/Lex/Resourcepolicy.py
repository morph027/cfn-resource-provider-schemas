SCHEMA = {
  "typeName" : "AWS::Lex::ResourcePolicy",
  "description" : "A resource policy with specified policy statements that attaches to a Lex bot or bot alias.",
  "sourceUrl" : "https://docs.aws.amazon.com/lexv2/latest/dg/security_iam_service-with-iam.html#security_iam_service-with-iam-resource-based-policies",
  "definitions" : {
    "ResourceArn" : {
      "description" : "The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1011
    },
    "Policy" : {
      "description" : "A resource policy to add to the resource. The policy is a JSON structure following the IAM syntax that contains one or more statements that define the policy.",
      "type" : "object"
    },
    "RevisionId" : {
      "description" : "The current revision of the resource policy. Use the revision ID to make sure that you are updating the most current version of a resource policy when you add a policy statement to a resource, delete a resource, or update a resource.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 5,
      "pattern" : "^[0-9]+$"
    },
    "PhysicalId" : {
      "description" : "The Physical ID of the resource policy.",
      "type" : "string"
    }
  },
  "properties" : {
    "ResourceArn" : {
      "$ref" : "#/definitions/ResourceArn"
    },
    "RevisionId" : {
      "$ref" : "#/definitions/RevisionId"
    },
    "Policy" : {
      "$ref" : "#/definitions/Policy"
    },
    "Id" : {
      "$ref" : "#/definitions/PhysicalId"
    }
  },
  "taggable" : False,
  "additionalProperties" : False,
  "required" : [ "ResourceArn", "Policy" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "additionalIdentifiers" : [ [ "/properties/ResourceArn" ] ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/RevisionId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "lex:CreateResourcePolicy", "lex:DescribeResourcePolicy" ]
    },
    "read" : {
      "permissions" : [ "lex:DescribeResourcePolicy" ]
    },
    "update" : {
      "permissions" : [ "lex:UpdateResourcePolicy", "lex:DescribeResourcePolicy" ]
    },
    "delete" : {
      "permissions" : [ "lex:DeleteResourcePolicy", "lex:DescribeResourcePolicy" ]
    },
    "list" : {
      "permissions" : [ "lex:DescribeResourcePolicy" ]
    }
  }
}