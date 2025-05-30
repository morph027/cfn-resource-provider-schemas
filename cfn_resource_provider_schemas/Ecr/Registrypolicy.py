SCHEMA = {
  "typeName" : "AWS::ECR::RegistryPolicy",
  "description" : "The ``AWS::ECR::RegistryPolicy`` resource creates or updates the permissions policy for a private registry.\n A private registry policy is used to specify permissions for another AWS-account and is used when configuring cross-account replication. For more information, see [Registry permissions](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html) in the *Amazon Elastic Container Registry User Guide*.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ecr.git",
  "definitions" : {
    "RegistryId" : {
      "type" : "string",
      "description" : "The registry id.",
      "minLength" : 12,
      "maxLength" : 12,
      "pattern" : "^[0-9]{12}$"
    }
  },
  "properties" : {
    "RegistryId" : {
      "$ref" : "#/definitions/RegistryId",
      "description" : ""
    },
    "PolicyText" : {
      "type" : "object",
      "description" : "The JSON policy text for your registry."
    }
  },
  "required" : [ "PolicyText" ],
  "readOnlyProperties" : [ "/properties/RegistryId" ],
  "primaryIdentifier" : [ "/properties/RegistryId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ecr:GetRegistryPolicy", "ecr:PutRegistryPolicy" ]
    },
    "read" : {
      "permissions" : [ "ecr:GetRegistryPolicy" ]
    },
    "list" : {
      "permissions" : [ "ecr:GetRegistryPolicy" ]
    },
    "update" : {
      "permissions" : [ "ecr:GetRegistryPolicy", "ecr:PutRegistryPolicy" ]
    },
    "delete" : {
      "permissions" : [ "ecr:DeleteRegistryPolicy" ]
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "additionalProperties" : False
}