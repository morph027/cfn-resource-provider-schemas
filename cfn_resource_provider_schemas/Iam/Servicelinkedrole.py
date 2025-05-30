SCHEMA = {
  "typeName" : "AWS::IAM::ServiceLinkedRole",
  "description" : "Resource Type definition for AWS::IAM::ServiceLinkedRole",
  "additionalProperties" : False,
  "properties" : {
    "RoleName" : {
      "description" : "The name of the role.",
      "type" : "string"
    },
    "CustomSuffix" : {
      "description" : "A string that you provide, which is combined with the service-provided prefix to form the complete role name.",
      "type" : "string"
    },
    "Description" : {
      "description" : "The description of the role.",
      "type" : "string"
    },
    "AWSServiceName" : {
      "description" : "The service principal for the AWS service to which this role is attached.",
      "type" : "string"
    }
  },
  "required" : [ ],
  "createOnlyProperties" : [ "/properties/CustomSuffix", "/properties/AWSServiceName" ],
  "primaryIdentifier" : [ "/properties/RoleName" ],
  "readOnlyProperties" : [ "/properties/RoleName" ],
  "writeOnlyProperties" : [ "/properties/CustomSuffix", "/properties/AWSServiceName" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:CreateServiceLinkedRole", "iam:GetRole" ]
    },
    "read" : {
      "permissions" : [ "iam:GetRole" ]
    },
    "update" : {
      "permissions" : [ "iam:UpdateRole", "iam:GetRole" ]
    },
    "delete" : {
      "permissions" : [ "iam:DeleteServiceLinkedRole", "iam:GetServiceLinkedRoleDeletionStatus", "iam:GetRole" ]
    }
  }
}