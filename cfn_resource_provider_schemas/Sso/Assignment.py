SCHEMA = {
  "typeName" : "AWS::SSO::Assignment",
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False
  },
  "description" : "Resource Type definition for SSO assignmet",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-sso/aws-sso-assignment",
  "properties" : {
    "InstanceArn" : {
      "description" : "The sso instance that the permission set is owned.",
      "type" : "string",
      "pattern" : "arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}",
      "minLength" : 10,
      "maxLength" : 1224
    },
    "TargetId" : {
      "description" : "The account id to be provisioned.",
      "type" : "string",
      "pattern" : "\\d{12}"
    },
    "TargetType" : {
      "description" : "The type of resource to be provsioned to, only aws account now",
      "type" : "string",
      "enum" : [ "AWS_ACCOUNT" ]
    },
    "PermissionSetArn" : {
      "description" : "The permission set that the assignemt will be assigned",
      "type" : "string",
      "pattern" : "arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::permissionSet/(sso)?ins-[a-zA-Z0-9-.]{16}/ps-[a-zA-Z0-9-./]{16}",
      "minLength" : 10,
      "maxLength" : 1224
    },
    "PrincipalType" : {
      "description" : "The assignee's type, user/group",
      "type" : "string",
      "enum" : [ "USER", "GROUP" ]
    },
    "PrincipalId" : {
      "description" : "The assignee's identifier, user id/group id",
      "type" : "string",
      "pattern" : "^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$",
      "minLength" : 1,
      "maxLength" : 47
    }
  },
  "additionalProperties" : False,
  "required" : [ "InstanceArn", "TargetId", "TargetType", "PermissionSetArn", "PrincipalType", "PrincipalId" ],
  "createOnlyProperties" : [ "/properties/InstanceArn", "/properties/TargetId", "/properties/TargetType", "/properties/PermissionSetArn", "/properties/PrincipalType", "/properties/PrincipalId" ],
  "primaryIdentifier" : [ "/properties/InstanceArn", "/properties/TargetId", "/properties/TargetType", "/properties/PermissionSetArn", "/properties/PrincipalType", "/properties/PrincipalId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "sso:CreateAccountAssignment", "sso:DescribeAccountAssignmentCreationStatus", "sso:ListAccountAssignments", "iam:GetSAMLProvider", "iam:CreateSAMLProvider", "iam:AttachRolePolicy", "iam:PutRolePolicy", "iam:CreateRole", "iam:ListRolePolicies" ]
    },
    "read" : {
      "permissions" : [ "sso:ListAccountAssignments", "iam:GetSAMLProvider", "iam:ListRolePolicies" ]
    },
    "delete" : {
      "permissions" : [ "sso:ListAccountAssignments", "sso:DeleteAccountAssignment", "sso:DescribeAccountAssignmentDeletionStatus", "iam:GetSAMLProvider", "iam:ListRolePolicies" ]
    },
    "list" : {
      "permissions" : [ "sso:ListAccountAssignments", "iam:ListRolePolicies" ]
    }
  }
}