SCHEMA = {
  "typeName" : "AWS::VpcLattice::AuthPolicy",
  "description" : "Creates or updates the auth policy.",
  "additionalProperties" : False,
  "properties" : {
    "ResourceIdentifier" : {
      "type" : "string",
      "pattern" : "^((((sn)|(svc))-[0-9a-z]{17})|(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(service/svc))-[0-9a-z]{17}))$",
      "maxLength" : 200,
      "minLength" : 17
    },
    "Policy" : {
      "type" : "object"
    },
    "State" : {
      "type" : "string",
      "enum" : [ "ACTIVE", "INACTIVE" ]
    }
  },
  "required" : [ "ResourceIdentifier", "Policy" ],
  "readOnlyProperties" : [ "/properties/State" ],
  "createOnlyProperties" : [ "/properties/ResourceIdentifier" ],
  "primaryIdentifier" : [ "/properties/ResourceIdentifier" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "vpc-lattice:GetAuthPolicy", "vpc-lattice:PutAuthPolicy" ]
    },
    "read" : {
      "permissions" : [ "vpc-lattice:GetAuthPolicy" ]
    },
    "update" : {
      "permissions" : [ "vpc-lattice:GetAuthPolicy", "vpc-lattice:PutAuthPolicy" ]
    },
    "delete" : {
      "permissions" : [ "vpc-lattice:GetAuthPolicy", "vpc-lattice:DeleteAuthPolicy" ]
    }
  },
  "tagging" : {
    "taggable" : False
  }
}